# Timescribe

## Installation Guide

After downloading the repo, create a virtual environment. This is so that the installations do not conflict with your base Python interpreter. I usually run:

```
python -m venv env
```

But you can use other tools like conda for the job. Once the virtual environment is created, activate it. In windows, you do:

```
.\env\Scripts\activate
```

and in Linux, you do:

```
source ./env/bin/activate
```

I don't use Mac, so I don't know how to do it in Mac, but there should be tutorials.

After activating the virtual environment, you are good to start installing the necessary libraries with:

```
pip install -r requirements.txt
```

This should install everything you need. To enable CUDA and run the model on your GPU however, you might need to reinstall torch with the CUDA toolkit, as I'm not sure if that is retained inside the requirements.txt

You can do it with this command:

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

Or just use the [official Pytorch installation](https://pytorch.org/get-started/locally/) for your specific CUDA version. After this, you should be good to go!

## Usage

For now, the script can be run by executing the `main.py` file. I do have plan on turning this into a CLI application, so I will update the guide when I do so.