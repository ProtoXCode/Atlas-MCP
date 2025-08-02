import subprocess


def test_ollama_installed():
    result = subprocess.run(["ollama", "--version"],
                            capture_output=True,
                            text=True)
    assert result.returncode == 0
    assert "ollama" in result.stdout.lower()
