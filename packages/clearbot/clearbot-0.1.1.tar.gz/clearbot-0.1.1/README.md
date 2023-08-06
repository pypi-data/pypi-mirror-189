# clearbot

Clearbit Logo API client.

`clearbot` fetches the logo of company (png file) based on their domain name.

## Install

The script in available through a python package.

```shell
pip install clearbot
```

## Get started

You can run directly the script on a domain.

```shell
clearbot github.com
```

You can pass several domains as well.

```shell
clearbot github.com gitlab.com
```

By default it will output `/tmp/github.com.png`. You can change the destination directory with the `-o` option.

```shell
clearbot -o . github.com
```

By default it outputs 512px png file (i.e. the greatest side has 512px). You can change it with the `-s` option.

```shell
clearbot -s 128 github.com
```

Finally sometimes we may want to remove the white background (transparence). For this purpose, you can use the `-t` options that thresholds the whites (it must between 0 and 255 as it is applied on a grayscale version of the image).

```shell
clearbot -t 250 github.com
```

## What's next?

- Use a file as input
- Colorize image
