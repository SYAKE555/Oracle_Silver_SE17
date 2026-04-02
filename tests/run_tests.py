#!/usr/bin/env python3
"""
Basetract Test Execution Suite
"""

import sys
import os
import subprocess
import time
from pathlib import Path

def _subprocess_env():
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return env

def run_syntax_checks():
    """Python構文チェック"""
    print("🔍 Running syntax checks...")
    
    python_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    failed_files = []
    for file_path in python_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                src = f.read()
            compile(src, file_path, 'exec')
        except Exception as e:
            failed_files.append((file_path, str(e)))
    
    if failed_files:
        print("❌ Syntax errors found:")
        for file_path, error in failed_files:
            print(f"  {file_path}: {error}")
        return False
    print("✅ All syntax checks passed")
    return True

def run_unit_tests():
    """単体テスト実行"""
    print("🧪 Running unit tests...")
    test_file = Path(__file__).parent / 'test_comprehensive.py'
    if not test_file.exists():
        print("❌ Test file not found")
        return False
    
    result = subprocess.run(
        [sys.executable, str(test_file)],
        capture_output=True,
        text=True,
        env=_subprocess_env()
    )
    if result.returncode != 0:
        print("❌ Unit tests failed")
        print(result.stdout)
        print(result.stderr)
        return False
    print("✅ All unit tests passed")
    return True

def run_integration_tests():
    """統合テスト実行"""
    print("🔗 Running integration tests...")
    tests = [
        ('Network Config', 'from network_config import NetworkConfig; NetworkConfig.get_server_url()'),
        ('Import Manager', 'from import_manager import get_project_root; print(get_project_root())'),
    ]
    
    for name, test_code in tests:
        cmd = [sys.executable, '-c', f'import sys; sys.path.insert(0, "pipeline/tools"); {test_code}']
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10, env=_subprocess_env())
        if result.returncode != 0:
            print(f"❌ {name} failed: {result.stderr}")
            return False
    print("✅ All integration tests passed")
    return True

def run_performance_tests():
    """パフォーマンステスト"""
    print("⚡ Running performance tests...")
    start = time.time()
    cmd = [sys.executable, '-c', 'import sys; sys.path.insert(0, "pipeline/tools"); from network_config import NetworkConfig; [NetworkConfig.get_flask_config() for _ in range(100)]']
    result = subprocess.run(cmd, capture_output=True, text=True, env=_subprocess_env())
    duration = time.time() - start
    if result.returncode == 0:
        print(f"✅ Performance test passed: {duration:.3f}s")
        return True
    return False

def run_security_tests():
    """セキュリティテスト"""
    print("🔒 Running security tests...")
    sensitive_patterns = ['SECRET_KEY=', 'API_KEY=', 'PASSWORD=']
    exclude_dirs = ['test', 'docs', 'pipeline/logs', 'config']
    exclude_exts = ['.md', '.html', '.txt', '.json', '.env']
    
    issues = []
    for root, dirs, files in os.walk('.'):
        # 除外ディレクトリのパスをチェック
        parts = Path(root).parts
        if any(p.lower() in exclude_dirs for p in parts):
            continue
            
        for file in files:
            path = os.path.join(root, file)
            # 自身（run_tests.py）をスキップ
            if os.path.abspath(path) == os.path.abspath(__file__):
                continue
            if not file.endswith('.py') or any(file.endswith(ext) for ext in exclude_exts):
                continue
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line_no, line in enumerate(f, 1):
                        if any(p in line for p in sensitive_patterns):
                            # 環境変数参照、コメント、または export コマンドをスキップ
                            if 'os.getenv' in line or 'os.environ' in line or line.strip().startswith('#') or 'export ' in line:
                                continue
                            issues.append(f"{path}:{line_no} -> {line.strip()}")
            except Exception:
                continue
    
    if issues:
        print("❌ Security issues found:")
        for issue in issues:
            print(f"  {issue}")
        return False
    print("✅ No security issues found")
    return True

def main():
    print("🚀 Basetract Automated Test Suite")
    print("=" * 50)
    tests = [
        ("Syntax", run_syntax_checks),
        ("Unit", run_unit_tests),
        ("Integration", run_integration_tests),
        ("Performance", run_performance_tests),
        ("Security", run_security_tests),
    ]
    
    results = []
    for name, func in tests:
        print(f"\n📋 {name}")
        results.append((name, func()))
    
    print("\n📊 Summary")
    passed = sum(1 for _, r in results if r)
    for name, r in results:
        status = "PASSED" if r else "FAILED"
        print(f"{name:<15} {status}")
    
    return 0 if passed == len(tests) else 1

if __name__ == '__main__':
    sys.exit(main())
