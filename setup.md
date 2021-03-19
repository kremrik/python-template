## How I set up my Python environment
So, for starters, I use Miniconda.
It's sort of a holdover from when I worked in analytics, but I've come to appreciate its simplicity.
Don't @ me.

### Setup
***SIGH*** Python's dependency management is...not glamorous.
This might seem complicated compared to other languages, but this method gives you complete and full control.
You'll appreciate this if you ever install a corrupt dependency...

#### 1. Download Miniconda
I usually just go to this link to grab the URL of the script: https://docs.conda.io/en/latest/miniconda.html
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Check that hash!
```
sha256sum Miniconda3-latest-Linux-x86_64.sh
```
Should match the hash next to the version of Miniconda you downloaded from link above.

#### 2. Run install script
```bash
bash Miniconda3-latest-Linux-x86_64.sh
```

It'll ask you to accept the license and whatnot, and ask you to confirm the default install location (usually $HOME).
At the end it'll probably ask if you want to add conda to your path.
I always hit NO, because I don't want anything messing with my `.bashrc`.
If you were planning on using miniconda specify for its `conda` dependency resolver, you are more than welcome to hit YES.

#### 3. Prepend miniconda's Python to your path
Something like this in your `.bashrc` should suffice
```bash
export PATH=~/miniconda3/bin:$PATH
```

Once you source your `.bashrc`, you should then see the miniconda Python by default:
```bash
$ which python
/home/[your-user]/miniconda3/bin/python
```

### Using
Once the steps above are complete, you should be able to create environments and install 3rd-party libraries using `pip` or `conda`.

#### Create environment
```bash
conda create -n test-env pip
```

The above command will create a new conda environment and install `pip` to it immediately.
The `pip` part is there to ensure that when `pip` installing to that env, it installs to the correct location.
Once that's created, you can activate:
```bash
source activate test-env
```

And then verify that the correct `pip` is being used:
```bash
$ which pip
/home/[your-user]/miniconda3/envs/test-env/bin/pip
```

If you see all that, you're home free.

#### Install module(s)
For example, installing pytest:
```bash
pip install pytest
```

That's it.

#### Examine the environment
This part isn't strictly necessary, but it's helpful to see what's going on.
This is where all of your environments live:
```bash
$ ls -lth /home/[your-user]/miniconda3/envs
drwxrwxr-x 10 your-user your-user 4.0K Mar 13 20:43 test-env
```

You can drill down into this to find modules installed:
```bash
$ ls -lth /home/[your-user]/miniconda3/envs/test-env/bin
...
drwxrwxr-x 10 your-user your-user 4.0K Mar 13 20:43 python
...
drwxrwxr-x 10 your-user your-user 4.0K Mar 13 20:43 pytest
...
```

If there's ever a problem with dependencies or corruption, you can always `rm -rf` the crap out of things here.
You'll also notice that `python` shows up under the above `env/bin`.
If you're using an IDE like PyCharm, you can point it to existing environments by giving it this path (`/home/[your-user]/miniconda3/envs/test-env/bin/python`)
