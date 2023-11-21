import subprocess

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class PromptReq(BaseModel):
    data: str


class PromptResp(BaseModel):
    data: str


@app.post("/v1/prompt/")
def create_prompt(prompt: PromptReq) -> PromptResp:
    # Send prompt to LLM model
    cmd: str = f'cd llama/llama.cpp && ./main -m ./models/llama-2-13b-chat.ggmlv3.q4_0.gguf.bin -p "{prompt}"'
    output: str = subprocess.getoutput(cmd)

    # Sanitize result
    response: str = (
        output.split(prompt.data)[1].split("[end of text]")[0].replace("\n", "").strip()
    )

    print(prompt)
    print(output)
    print(response)

    return PromptResp(data=response)


def main() -> None:
    print("started")


if __name__ == "__main__":
    main()
