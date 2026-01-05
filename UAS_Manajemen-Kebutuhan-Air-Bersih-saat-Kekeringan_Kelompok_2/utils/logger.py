import logging


def setup_logger():
    """
    Mengkonfigurasi dan membuat logger untuk aplikasi.

    Mengatur format log dengan timestamp, level, dan pesan.
    Logger dikonfigurasi dengan level INFO untuk mencatat
    semua aktivitas penting dalam sistem.

    Returns:
        logging.Logger: Instance logger yang sudah dikonfigurasi
    """
    # Mengatur format log
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logging.getLogger("WaterSystem")


logger = setup_logger()
