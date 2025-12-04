# 
# # ✅ 3. PRODUCTIVITY STATS

# “I want analytics over time”

# Stats to include

# ✔ Tasks completed this week
# ✔ Tasks completed this month
# ✔ Tasks completed per category
# ✔ Streak count
# ✔ Weekly productivity trend
# 
# 
# @stats_bp.route('/<int:user_id>', methods=['GET'])
# def get_stats(user_id):
#     today = date.today()
#     week_ago = today - timedelta(days=7)
#     month_ago = today - timedelta(days=30)

#     completed_today = Task_history.query.filter(
#         Task_history.user_id == user_id,
#         db.func.date(Task_history.completed_at) == today
#     ).count()




# ✅ 4. AUTOSAVE (Backend Support)
# Requirement

# Whenever user is typing/editing:

# Save changes instantly

# No “save” button

# Backend Support

# PATCH /tasks/<id>/autosave

# Frontend

# Send PATCH every time input stops for 300ms.

# Backend Implementation


# @tasks_bp.route('/autosave/<int:id>', methods=['PATCH'])
# def autosave_task(id):
#     task = Task.query.get(id)
#     if not task:
#         return {"error": "Task not found"}, 404

#     data = request.json
#     for key, value in data.items():
#         setattr(task, key, value)

#     db.session.commit()
#     return {"message": "autosaved"}, 200



