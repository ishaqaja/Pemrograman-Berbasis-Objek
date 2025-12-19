import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass


# === KONFIGURASI LOGGING (WAJIB DI PALING ATAS FILE) ===
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)

LOGGER = logging.getLogger("Checkout")


# === MODEL SEDERHANA ===
@dataclass
class Order:
    customer_name: str
    total_price: float
    status: str = "open"


# === KODE BURUK (SEBELUM REFACTOR) ===
class OrderManager:
    """
    Contoh implementasi buruk yang melanggar prinsip SRP, OCP, dan DIP.
    """

    def process_checkout(self, order: Order, payment_method: str):
        LOGGER.info(f"Memulai checkout untuk {order.customer_name}")

        if payment_method == "credit card":
            LOGGER.info("Processing Credit Card")
        elif payment_method == "bank transfer":
            LOGGER.info("Processing Bank Transfer")
        else:
            LOGGER.error("Metode pembayaran tidak valid")
            return False

        LOGGER.info(f"Mengirim notifikasi ke {order.customer_name}")
        order.status = "paid"
        return True


# === ABSTRAKSI (KONTRAK UNTUK OCP & DIP) ===
class IPaymentProcessor(ABC):
    """Kontrak untuk semua processor pembayaran."""

    @abstractmethod
    def process(self, order: Order) -> bool:
        pass


class INotificationService(ABC):
    """Kontrak untuk semua layanan notifikasi."""

    @abstractmethod
    def send(self, order: Order):
        pass


# === IMPLEMENTASI KONKRIT ===
class CreditCardProcessor(IPaymentProcessor):
    """Implementasi pembayaran menggunakan kartu kredit."""

    def process(self, order: Order) -> bool:
        LOGGER.info("Payment: Memproses Kartu Kredit")
        return True


class EmailNotifier(INotificationService):
    """Implementasi notifikasi melalui email."""

    def send(self, order: Order):
        LOGGER.info(f"Notif: Email konfirmasi dikirim ke {order.customer_name}")


# === KELAS KOORDINATOR (SRP & DIP) ===
class CheckoutService:
    """
    Kelas high-level untuk mengoordinasikan proses checkout pesanan.

    Kelas ini mengatur alur pembayaran dan notifikasi tanpa mengetahui
    detail implementasinya (SRP & DIP).
    """

    def __init__(self, payment_processor: IPaymentProcessor, notifier: INotificationService):
        """
        Menginisialisasi CheckoutService dengan dependensi yang diperlukan.
        """
        self.payment_processor = payment_processor
        self.notifier = notifier

    def run_checkout(self, order: Order) -> bool:
        """
        Menjalankan proses checkout dan memvalidasi pembayaran.
        """
        LOGGER.info(
            f"Memulai checkout | Customer: {order.customer_name} | Total: {order.total_price}"
        )

        payment_success = self.payment_processor.process(order)

        if payment_success:
            order.status = "paid"
            self.notifier.send(order)
            LOGGER.info("Checkout sukses | Status pesanan: PAID")
            return True
        else:
            LOGGER.error("Pembayaran gagal | Transaksi dibatalkan")
            return False


# === PROGRAM UTAMA ===
andi_order = Order("Andi", 500000)
email_service = EmailNotifier()

# Skenario 1: Credit Card
cc_processor = CreditCardProcessor()
checkout_cc = CheckoutService(cc_processor, email_service)

LOGGER.info("--- Skenario 1: Credit Card ---")
checkout_cc.run_checkout(andi_order)


# Pembuktian OCP: QRIS
class QrisProcessor(IPaymentProcessor):
    """Implementasi pembayaran menggunakan QRIS."""

    def process(self, order: Order) -> bool:
        LOGGER.info("Payment: Memproses QRIS")
        return True


budi_order = Order("Budi", 100000)
qris_processor = QrisProcessor()

checkout_qris = CheckoutService(qris_processor, email_service)

LOGGER.info("--- Skenario 2: Pembuktian OCP (QRIS) ---")
checkout_qris.run_checkout(budi_order)
