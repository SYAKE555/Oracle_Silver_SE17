#!/usr/bin/env python3
"""
Basetract Comprehensive Test Suite — Complete Quality Assurance
全システムの品質を保証する包括的テストスイート
"""

import unittest
import json
import os
import sys
import tempfile
import subprocess
import unittest.mock
from pathlib import Path
from unittest.mock import patch, MagicMock

# centralized import manager を使用
import os, sys
from pathlib import Path

# Add tools directory to path robustly
tools_dir = str(Path(__file__).resolve().parent.parent / 'pipeline' / 'tools')
if tools_dir not in sys.path:
    sys.path.insert(0, tools_dir)

try:
    from import_manager import setup_tools_import
    setup_tools_import()
except ImportError:
    pass

class TestNetworkConfig(unittest.TestCase):
    """ネットワーク設定モジュールのテスト"""
    
    def setUp(self):
        from network_config import NetworkConfig
        self.config = NetworkConfig()
    
    def test_flask_config_default_values(self):
        """Flask設定のデフォルト値テスト"""
        config = self.config.get_flask_config()
        self.assertEqual(config['host'], '127.0.0.1')
        self.assertEqual(config['port'], 5000)
        self.assertFalse(config['debug'])
        self.assertIn('cors_origins', config)
    
    def test_timeout_config_values(self):
        """タイムアウト設定のテスト"""
        config = self.config.get_timeout_config()
        self.assertIn('flask_startup', config)
        self.assertIn('crawler_request', config)
        self.assertIn('ocr_request', config)
        self.assertTrue(all(isinstance(v, int) for v in config.values()))
    
    def test_crawler_config_values(self):
        """クローラー設定のテスト"""
        config = self.config.get_crawler_config()
        self.assertIn('min_delay', config)
        self.assertIn('max_delay', config)
        self.assertIn('user_agents', config)
        self.assertLessEqual(config['min_delay'], config['max_delay'])
    
    def test_server_url_generation(self):
        """サーバーURL生成のテスト"""
        url = self.config.get_server_url()
        self.assertEqual(url, "http://127.0.0.1:5000")
    
    @patch.dict(os.environ, {'FLASK_HOST': '0.0.0.0', 'FLASK_PORT': '8080'})
    def test_environment_override(self):
        """環境変数による設定上書きのテスト"""
        config = self.config.get_flask_config()
        self.assertEqual(config['host'], '0.0.0.0')
        self.assertEqual(config['port'], 8080)

class TestQualityConfig(unittest.TestCase):
    """品質設定モジュールのテスト"""
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.profiles_path = os.path.join(self.temp_dir, 'quality_profiles.json')
        
        # テスト用設定ファイルを作成
        test_config = {
            "active_profile": "test",
            "profiles": {
                "test": {
                    "name": "Test Profile",
                    "logic": {
                        "critical_chars": 30,
                        "recommended_chars": 80,
                        "tech_fact_min_count": 2,
                        "official_excerpt_bypass": True
                    },
                    "ocr": {
                        "confidence_min": 0.65,
                        "noise_ratio_max": 0.15
                    }
                }
            }
        }
        
        with open(self.profiles_path, 'w', encoding='utf-8') as f:
            json.dump(test_config, f, ensure_ascii=False, indent=2)
    
    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir)
    
    @patch('quality_config._PROFILES_PATH')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_load_config_success(self, mock_open_file, mock_path):
        """設定ファイル読み込み成功のテスト"""
        mock_path.__str__.return_value = str(self.profiles_path)
        mock_path.exists.return_value = True
        
        # モックファイルの内容を設定
        mock_open_file.return_value.read.return_value = json.dumps({
            "active_profile": "test",
            "profiles": {
                "test": {
                    "name": "Test Profile",
                    "logic": {"critical_chars": 30}
                }
            }
        })
        
        from quality_config import load_config
        config = load_config()
        
        self.assertEqual(config['active_profile'], 'test')
        self.assertIn('profiles', config)
        self.assertIn('test', config['profiles'])
    
    @patch('quality_config._PROFILES_PATH')
    def test_load_config_file_not_found(self, mock_path):
        """設定ファイル不存在時のテスト"""
        mock_path.__str__.return_value = '/nonexistent/path'
        mock_path.exists.return_value = False
        
        from quality_config import load_config
        with self.assertRaises(FileNotFoundError):
            load_config()
    
    @patch('quality_config._PROFILES_PATH')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_load_config_invalid_json(self, mock_open_file, mock_path):
        """不正JSONファイルのテスト"""
        mock_path.__str__.return_value = str(self.profiles_path)
        mock_path.exists.return_value = True
        
        # 不正JSONをモック
        mock_open_file.return_value.read.return_value = '{"invalid": json}'
        
        from quality_config import load_config
        with self.assertRaises(ValueError):
            load_config()

class TestProfileLoader(unittest.TestCase):
    """プロファイルローダーのテスト"""
    
    @patch('profile_loader.load_quality_profile')
    def test_get_critical_chars(self, mock_load):
        """クリティカル文字数取得のテスト"""
        mock_load.return_value = {
            'logic': {'critical_chars': 45}
        }
        
        from profile_loader import get_critical_chars
        result = get_critical_chars()
        self.assertEqual(result, 45)
    
    @patch('profile_loader.load_quality_profile')
    def test_get_ocr_confidence_min(self, mock_load):
        """OCR最低信頼度取得のテスト"""
        mock_load.return_value = {
            'ocr': {'confidence_min': 0.75}
        }
        
        from profile_loader import get_ocr_confidence_min
        result = get_ocr_confidence_min()
        self.assertEqual(result, 0.75)

class TestQualityGuard(unittest.TestCase):
    """品質ガードのテスト"""
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_data = [
            {
                "id": "test-1",
                "category": "Test",
                "text": "This is a test question with sufficient technical content including specific protocols and numerical values.",
                "type": "choice",
                "answer": "A",
                "options": ["A. Correct", "B. Wrong", "C. Wrong", "D. Wrong"],
                "logic": "The correct answer is A because it aligns with RFC 791 which specifies IP version 4 protocol details.",
                "plan": "Study IP addressing fundamentals",
                "weight": 0.1,
                "textbook_ref": ["TCP/IP Illustrated"],
                "tags": ["networking"],
                "difficulty": "medium"
            }
        ]
        
        self.test_file = os.path.join(self.temp_dir, 'test_data.json')
        with open(self.test_file, 'w', encoding='utf-8') as f:
            json.dump(self.test_data, f, ensure_ascii=False, indent=2)
    
    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir)
    
    @patch('profile_loader.load_quality_profile')
    def test_validate_structure_success(self, mock_load):
        """構造検証成功のテスト"""
        mock_load.return_value = {
            'logic': {'critical_chars': 40, 'recommended_chars': 100, 'tech_fact_min_count': 3, 'official_excerpt_bypass': True},
            'schema': {'missing_keys_level': 'error', 'answer_in_options_strict': True}
        }
        
        from quality_guard import QualityGuard
        guard = QualityGuard(self.test_file)
        result = guard.validate_structure()
        self.assertTrue(result)
        self.assertEqual(len(guard.errors), 0)
    
    @patch('profile_loader.load_quality_profile')
    def test_validate_missing_keys(self, mock_load):
        """必須キー欠損のテスト"""
        mock_load.return_value = {
            'logic': {'critical_chars': 40, 'recommended_chars': 100, 'tech_fact_min_count': 3, 'official_excerpt_bypass': True},
            'schema': {'missing_keys_level': 'error', 'answer_in_options_strict': True}
        }
        
        # 不完全なデータを作成（必須キーを欠損）
        incomplete_data = [{"id": "test-1"}]  # text, type, answer, options, logic などが欠損
        incomplete_file = os.path.join(self.temp_dir, 'incomplete.json')
        with open(incomplete_file, 'w', encoding='utf-8') as f:
            json.dump(incomplete_data, f)
        
        from quality_guard import QualityGuard
        guard = QualityGuard(incomplete_file)
        # 構造自体は正しい（リスト形式）ので True を返す
        struct_result = guard.validate_structure()
        self.assertTrue(struct_result)
        
        # 粒度（スキーマ）検証を実行
        guard.validate_granularity()
        
        # エラー（欠損キー）が検出されることを確認
        self.assertGreater(len(guard.errors), 0)
        
        # エラーメッセージの内容を確認
        error_messages = ' '.join(guard.errors)
        self.assertTrue(
            any(keyword in error_messages.lower() for keyword in ['missing', 'required', 'keys', '必須', '欠損'])
        )

class TestImportManager(unittest.TestCase):
    """インポートマネージャーのテスト"""
    
    def test_get_project_root(self):
        """プロジェクトルート取得のテスト"""
        from import_manager import get_project_root
        root = get_project_root()
        self.assertIsInstance(root, Path)
        self.assertEqual(root.name, 'pipeline')
    
    def test_setup_tools_import(self):
        """ツールインポート設定のテスト"""
        from import_manager import setup_tools_import
        original_path = sys.path.copy()
        
        setup_tools_import()
        
        # パスが追加されたことを確認
        tools_path = str(Path(__file__).resolve().parent.parent / 'pipeline' / 'tools')
        self.assertIn(tools_path, sys.path)
        
        # 重複追加されないことを確認
        setup_tools_import()
        self.assertEqual(sys.path.count(tools_path), 1)
        
        sys.path = original_path

class TestSystemIntegration(unittest.TestCase):
    """システム統合テスト"""

    def _assert_python_compiles(self, file_path: str, label: str):
        with open(file_path, 'r', encoding='utf-8') as f:
            src = f.read()
        try:
            compile(src, file_path, 'exec')
        except Exception as e:
            self.fail(f"{label} syntax error: {e}")
    
    def test_bootstrap_integration(self):
        """ブートストラップ統合テスト"""
        bootstrap_path = os.path.join(os.path.dirname(__file__), '..', 'pipeline', 'bootstrap.py')
        self._assert_python_compiles(bootstrap_path, "Bootstrap")
    
    def test_factory_integration(self):
        """ファクトリー統合テスト"""
        factory_path = os.path.join(os.path.dirname(__file__), '..', 'pipeline', 'tools', 'factory.py')
        self._assert_python_compiles(factory_path, "Factory")
    
    def test_app_integration(self):
        """アプリケーション統合テスト"""
        app_path = os.path.join(os.path.dirname(__file__), '..', 'app.py')
        self._assert_python_compiles(app_path, "App")

class TestPerformance(unittest.TestCase):
    """パフォーマンステスト"""
    
    def test_config_loading_performance(self):
        """設定読み込みパフォーマンステスト"""
        import time
        from network_config import NetworkConfig
        
        start_time = time.time()
        for _ in range(100):
            NetworkConfig.get_flask_config()
        end_time = time.time()
        
        # 100回の呼び出しが1秒以内に完了することを確認
        self.assertLess(end_time - start_time, 1.0)
    
    def test_profile_loading_performance(self):
        """プロファイル読み込みパフォーマンステスト"""
        import time
        
        with patch('profile_loader.load_quality_profile') as mock_load:
            mock_load.return_value = {'logic': {'critical_chars': 40}}
            
            start_time = time.time()
            for _ in range(50):
                from profile_loader import get_critical_chars
                get_critical_chars()
            end_time = time.time()
            
            # 50回の呼び出しが0.5秒以内に完了することを確認
            self.assertLess(end_time - start_time, 0.5)

if __name__ == '__main__':
    # テストスイート実行
    unittest.main(verbosity=2)
