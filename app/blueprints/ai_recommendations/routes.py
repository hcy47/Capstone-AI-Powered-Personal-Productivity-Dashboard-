@dashboard_bp.route('/<int:user_id>', methods=['GET'])
def daily_overview(user_id):
    today = date.today()

    tasks_today = Task.query.filter_by(user_id=user_id).filter(
        db.func.date(Task.due_date) == today
    ).all()

    upcoming_tasks = Task.query.filter_by(user_id=user_id).filter(
        Task.due_date > today
    ).order_by(Task.due_date).limit(5).all()

    categories = Category.query.filter_by(user_id=user_id).all()

    weather = get_weather_for_user(user_id)
    quote = get_daily_quote()

    return jsonify({
        "tasks_today": tasks_schema.dump(tasks_today),
        "upcoming_tasks": tasks_schema.dump(upcoming_tasks),
        "categories": categories_schema.dump(categories),
        "weather": weather,
        "quote": quote
    }), 200