import argparse
import logging
from .core import ConvergenceEngine, EngineConfig

def main(argv=None):
    parser = argparse.ArgumentParser(prog="agentic-convergence")
    parser.add_argument("--steps", type=int, default=5)
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)
    cfg = EngineConfig(max_steps=args.steps, debug=args.debug)
    engine = ConvergenceEngine(cfg)
    result = engine.run({"initial": True})
    print("Run complete:", result)

if __name__ == "__main__":
    main()
