import chalk

def good(x):
    print(f"[👍] {chalk.green(x)}")

def danger(x):
    print(f"[👎] {chalk.red(x)}")

def warning(x):
    print(f"[📄] {chalk.yellow(x)}")

def info(x):
    print(f"[📣] {chalk.blue(x)}")

def log_account(username, email, password):
    with open('accounts.txt', 'a') as f:
        f.write(f"{email}:{username}:{password}\n")