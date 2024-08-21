from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, order_amount):
        pass

class RegularDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        # No discount for regular customers
        return order_amount

class PremiumDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        # 10% discount for premium customers
        return order_amount * 0.9

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        # 20% discount for VIP customers
        return order_amount * 0.8

class Order:
    def __init__(self, customer_type, order_amount):
        self.customer_type = customer_type
        self.order_amount = order_amount
        self.discount_strategy = self._get_discount_strategy()

    def _get_discount_strategy(self):
        if self.customer_type == "regular":
            return RegularDiscount()
        elif self.customer_type == "premium":
            return PremiumDiscount()
        elif self.customer_type == "vip":
            return VIPDiscount()
        else:
            raise ValueError("Unknown customer type")

    def final_price(self):
        return self.discount_strategy.apply_discount(self.order_amount)


if __name__ == "__main__":
    # Regular customer
    regular_order = Order("regular", 100)
    print(f"Final price for regular customer: ${regular_order.final_price()}")

    # Premium customer
    premium_order = Order("premium", 100)
    print(f"Final price for premium customer: ${premium_order.final_price()}")

    # VIP customer
    vip_order = Order("vip", 100)
    print(f"Final price for VIP customer: ${vip_order.final_price()}")

from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, order_amount):
        pass

class RegularDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount

class PremiumDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount * 0.9

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount * 0.8

class Order:
    def __init__(self, customer_type, order_amount):
        self.customer_type = customer_type
        self.order_amount = order_amount
        self.discount_strategy = self._get_discount_strategy()

    def _get_discount_strategy(self):
        if self.customer_type == "regular":
            return RegularDiscount()
        elif self.customer_type == "premium":
            return PremiumDiscount()
        elif self.customer_type == "vip":
            return VIPDiscount()
        else:
            raise ValueError("Unknown customer type")

    def final_price(self):
        return self.discount_strategy.apply_discount(self.order_amount)

if __name__ == "__main__":
    regular_order = Order("regular", 100)
    print(f"Final price for regular customer: ${regular_order.final_price()}")

    premium_order = Order("premium", 100)
    print(f"Final price for premium customer: ${premium_order.final_price()}")

    vip_order = Order("vip", 100)
    print(f"Final price for VIP customer: ${vip_order.final_price()}")
