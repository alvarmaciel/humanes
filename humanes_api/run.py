import argparse

import uvicorn

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Run ShipHero Warehouse Hero")

    parser.add_argument("--port", help="Port to run app on", default=8000, type=int)
    parser.add_argument("--host", help="Host to run app on", default="127.0.0.0")
    parser.add_argument("--log-level", help="Host to run app on", default="debug")

    args = parser.parse_args()

    uvicorn.run(
        "humanes.app:app",
        host=args.host,
        port=int(args.port),
        log_level=args.log_level,
        reload=True,
    )
