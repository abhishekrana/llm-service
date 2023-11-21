from fastapi import FastAPI

from resources.completions import CompletionsReq, ICompletions, CompletionsResp
from llama.completions import Completions


app = FastAPI()


@app.post("/v1/completions/")
def completions(req: CompletionsReq) -> CompletionsResp:
    completions: ICompletions | None = None
    if req.model == "llama2":
        completions = Completions()
    else:
        raise NotImplementedError

    resp: CompletionsResp = completions.create(req)
    return resp


def main() -> None:
    print("Started")


if __name__ == "__main__":
    main()
