class LibraryService:
    def __init__(self):
        self.inventory = {1042: 10}
        self.processed_transactions = []

    def return_book(self, transaction_id: str, book_id: int):
        # FIX: Ignore transaction if it was already processed
        if transaction_id in self.processed_transactions:
            return {"status": "ignored", "current_stock": self.inventory[book_id]}

        self.inventory[book_id] += 1
        self.processed_transactions.append(transaction_id)
        return {"status": "success", "current_stock": self.inventory[book_id]}

    def get_stock(self, book_id: int):
        return self.inventory.get(book_id, 0)