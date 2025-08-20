import subprocess
import pytest

def run_docker_psql(cmd):
    """
    Run a psql command inside the weshai_postgres container
    """
    full_cmd = [
        "docker", "exec", "-i", "weshai_postgres",
        "psql", "-U", "weshaiadmin", "-d", "WESHAI", "-t", "-c", cmd
    ]
    result = subprocess.run(full_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {result.stderr}")
    return result.stdout.strip().splitlines()

def test_weshai_database_exists():
    # List all databases
    output = run_docker_psql("SELECT datname FROM pg_database WHERE datistemplate = false;")
    
    print("Databases found in container:", output)
    
    assert "WESHAI" in [db.strip() for db in output], "WESHAI database was not created!"
