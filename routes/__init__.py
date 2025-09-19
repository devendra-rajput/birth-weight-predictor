from features.baby_weight.routes import predict_bp

# List of all blueprints to register
blueprints = [
    (predict_bp, '/')
]