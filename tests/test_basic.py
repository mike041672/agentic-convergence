from src import main

def test_main_runs(capsys):
    main.main()
    captured = capsys.readouterr()
    assert "Agentic Convergence engine" in captured.out