#!/usr/bin/env python

import os
import sys
import logging
import argparse
import requests
import io

import openai
from PIL import Image
from smartinput import Shell
from colorama import Style, Fore, init
from colorama.ansi import AnsiFore, code_to_chars

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', None)

if OPENAI_API_KEY is None:
    sys.exit("ERROR: Environment variable OPENAI_API_KEY not set (https://platform.openai.com/account/api-keys).  Exiting...")

# OpenAI Settings
DEF_ENGINE = os.getenv("OPENAI_DEFAULT_ENGINE", 'text-davinci-003')  # Also called models.  https://platform.openai.com/docs/models/overview
DEF_TEMP = int(os.getenv("OPENAI_DEFAULT_TEMPERATURE", .5))  # Creativity factory, 0 (less) to 1 (more) https://platform.openai.com/docs/api-reference/edits/create#edits/create-temperature
DEF_FREQ_PEN = int(os.getenv("OPENAI_DEFAULT_FREQUENCY_PENALTY", 0))  # -2 to 2.  Higher = Less likely to repeat.  https://platform.openai.com/docs/api-reference/completions/create#completions/create-frequency_penalty
DEF_PRESENCE_PEN = int(os.getenv("OPENAI_DEFAULT_PRESENCE_PENALTY", 0))  # -2 to 2.  Higher = More likely to discuss new topics.  https://platform.openai.com/docs/api-reference/completions/create#completions/create-presence_penalty
DEF_MAX_TOKENS = int(os.getenv("OPENAI_DEFAULT_MAX_TOKENS", 2048))  # Max tokens to generate in completion.   https://platform.openai.com/docs/api-reference/completions/create#completions/create-max_tokens
DEF_IMG_NUM = int(os.getenv("OPENAI_DEFAULT_IMAGE_NUMBER", 1))  # Number of images to return. Only supports 1 right now.
DEF_IMG_SIZE = os.getenv("OPENAI_DEFAULT_IMAGE_SIZE", "1024x1024")  # Resolution of image

# OAclI Settings
IN_COLOR = code_to_chars(getattr(AnsiFore, os.getenv("OACLI_INPUT_COLOR", "Green").upper())) + Style.BRIGHT
OUT_COLOR = code_to_chars(getattr(AnsiFore, os.getenv("OACLI_OUTPUT_COLOR", "Red").upper())) + Style.BRIGHT


class OpenAI:

    def __init__(
        self,
        engine=DEF_ENGINE,
        temperature=DEF_TEMP,
        frequency_penalty=DEF_FREQ_PEN,
        presence_penalty=DEF_PRESENCE_PEN,
        max_tokens=DEF_MAX_TOKENS,
        num_images=DEF_IMG_NUM,
        img_size=DEF_IMG_SIZE
    ):
        self.engine = engine
        self.temperature = temperature
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.max_tokens = max_tokens
        self.num_images = num_images
        self.img_size = img_size

    def _create_completion(self, prompt):
        return openai.Completion.create(
            engine=self.engine,
            prompt=prompt,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty
        )

    def _create_image(self, prompt):
        return openai.Image.create(
            prompt=prompt,
            n=self.num_images,
            max_tokens=self.max_tokens,
            size=self.img_size,
            temperature=self.temperature,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty
        )

    def get_image(self, prompt):
        response = self._create_image(prompt)

        image_url = response['data'][0]['url']
        image_data = requests.get(image_url).content
        image = Image.open(io.BytesIO(image_data))
        image.show()

    def get_resp(self, prompt):
        response = self._create_completion(prompt)

        print(response.choices[0].text.strip())

    def _handle_query(self, query, shell):
        if query in ('bye', 'quit', 'exit', 'leave', 'done', 'ciao') or self.tokens_used > self.max_tokens:
            shell.exit()

        if query in ('tokens'):
            shell.out(f"{self.tokens_used}/{self.max_tokens}")
            return

        if query in ('resp'):
            shell.out(str(self.last_resp))
            return

        self.convo.append(query)
        shell.alert("Thinking...")
        resp = self._create_completion(prompt="\n".join(self.convo))
        self.last_resp = resp
        self.convo.append(resp.choices[0].text.strip())
        self.tokens_used = resp.usage.total_tokens

        shell.out(self.convo[-1])

    def chat(self):
        self.convo = []
        self.last_resp = ""
        self.tokens_used = 0

        myshell = Shell(
            callback=self._handle_query,
            intitle=IN_COLOR + "me> ",
            outtitle=OUT_COLOR + "ai> ",
            inputcolor=IN_COLOR,
            outputcolor=OUT_COLOR,
            alertcolor=Fore.RED
        )
            
        myshell.start()


def main():
	
    parser = argparse.ArgumentParser(
        prog="oacli",
        description="OpenAI on the command line.  If no arguments are provided, you get a chat interface."
    )

    parser.add_argument("prompt", nargs='?', default='')
    parser.add_argument('-i', '--image', action='store_true', default=False, help="Bring up image from OpenAI.  Must provide prompt.")

    args = parser.parse_args()

    try:
        openai = OpenAI()

        if args.image:
            if not args.prompt:
                sys.exit("ERROR: No prompt provided.  Exiting...")
            openai.get_image(args.prompt)
        elif args.prompt:
            openai.get_resp(args.prompt)
        else:
            openai.chat()
    except KeyboardInterrupt:
        pass
    finally:
        print(Style.RESET_ALL)


if __name__ == "__main__":
    main()

