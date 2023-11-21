import subprocess

from resources.completions import ICompletions, CompletionsReq, CompletionsResp


class Completions(ICompletions):
    def create(self, request: CompletionsReq) -> CompletionsResp:
        if len(request.messages) > 1:
            raise NotImplementedError

        # Send to LLaMA
        cmd: str = f'cd llama/llama.cpp && ./main -m ./models/llama-2-13b-chat.ggmlv3.q4_0.gguf.bin -p "{request.messages[0].content}"'
        output: str = subprocess.getoutput(cmd)
        print(output)

        # Sanitize output
        content: str = (
            output.split(request.messages[0].content)[1]
            .split("[end of text]")[0]
            .replace("\n", "")
            .strip()
        )

        return CompletionsResp(content=content)
