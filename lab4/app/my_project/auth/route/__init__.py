from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.company_route import company_bp
    from .orders.parking_route import parking_bp
    from .orders.driver_route import driver_bp
    from .orders.car_route import car_bp
    from .orders.parking_lot_route import parking_lot_bp
    from .orders.parking_history_route import parking_history_bp
    from .orders.bonus_card_route import bonus_card_bp
    from .orders.reservation_route import reservation_bp
    from .orders.driver_and_bonus_card_route import driver_and_bonus_card_bp
    from .orders.company_and_bonus_card_route import company_and_bonus_card_bp
    from .orders.from_5th_lab_route import from_5th_lab_bp

    app.register_blueprint(company_bp)
    app.register_blueprint(parking_bp)
    app.register_blueprint(car_bp)
    app.register_blueprint(driver_bp)
    app.register_blueprint(parking_lot_bp)
    app.register_blueprint(parking_history_bp)
    app.register_blueprint(bonus_card_bp)
    app.register_blueprint(reservation_bp)
    app.register_blueprint(company_and_bonus_card_bp)
    app.register_blueprint(driver_and_bonus_card_bp)
    app.register_blueprint(from_5th_lab_bp)
