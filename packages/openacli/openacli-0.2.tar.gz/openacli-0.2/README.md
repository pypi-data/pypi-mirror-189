# OpenAclI
Wanted a tool to use OpenAI on the command line.  Also supports showing images.

## Installation
```bash
> pip install openacli
```

## Usage
You'll need an [OpenAI API key](https://platform.openai.com/account/api-keys) to use this library.

### Chat
```bash
> oacli
me> "<prompt with quotes>"
ai> <some response>
```

### Image
```bash
> oacli -i "<some prompt with quotes>"
```
Python Pillow will bring up and image

### Prompt
```bash
> oacli "<some prompt with quotes>"
<response from OpenAI>
```

## Settings
Several configuration settings are exposed through environment variables.  If they aren't provided, the defaults below will be applied.
```
# OpenAI Settings
OPENAI_DEFAULT_ENGINE="text-davinci-003"
OPENAI_DEFAULT_TEMPERATURE=.5
OPENAI_DEFAULT_FREQUENCY_PENALTY=0
OPENAI_DEFAULT_PRESENCE_PENALTY=0
OPENAI_DEFAULT_MAX_TOKENS=2048
OPENAI_DEFAULT_IMAGE_NUMBER=1
OPENAI_DEFAULT_IMAGE_SIZE="1024x1024"

# OAclI Settings
OACLI_INPUT_COLOR=Green
OACLI_OUTPUT_COLOR=Red
```

## Examples

### Chat
![image](https://user-images.githubusercontent.com/10888829/216837899-63139026-4653-4f83-817a-c8d0c39ca0e6.png)

### Image
![image](https://user-images.githubusercontent.com/10888829/216837652-99a70fa4-88f0-498b-ac1b-2a3703e90353.png)

### Prompt
![image](https://user-images.githubusercontent.com/10888829/216837814-468a2097-9e4f-46b5-b661-2cb3fd2d258f.png)



