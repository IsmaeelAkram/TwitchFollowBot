import chalk

def good(x):
    print(f"[👍] {chalk.green(x)}")

def danger(x):
    print(f"[👎] {chalk.red(x)}")

def warning(x):
    print(f"[📄] {chalk.yellow(x)}")

def info(x):
    print(f"[📣] {chalk.blue(x)}")