class InsufficientFundsError(Exception):
    pass

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._log = []
        return cls._instance

    def log(self, message):
        self._log.append(message)

    def get_logs(self):
        return self._log

class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0
        self.logger = Logger()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.logger.log(f"Внесено {amount} на рахунок{self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            self.logger.log(f"Невдала спроба вивести {amount} з рахунку {self.account_number}. Недостатньо коштів.")
            raise InsufficientFundsError("Insufficient funds for this withdrawal")
        self.balance -= amount
        self.logger.log(f"Сняли {amount} со счета {self.account_number}. Новый баланс: {self.balance}")

try:
    account = BankAccount("Anatoly Blinda")
    account.deposit(1000)
    account.withdraw(500)
    account.withdraw(600)  # Це викличе помилку InsufficientFundsError
except InsufficientFundsError as e:
    print(e)

logger = Logger()
for log in logger.get_logs():
    print(log)
