from app import LibraryService

def test_duplicate_return_idempotency():
    service = LibraryService()

    # First return request
    res1 = service.return_book("TXN-9981", 1042)
    assert res1["current_stock"] == 11

    # Duplicate network retry request
    res2 = service.return_book("TXN-9981", 1042)

    # Duplicate transaction should NOT increment stock again
    assert service.get_stock(1042) == 11, f"Expected stock 11, but got {service.get_stock(1042)}"