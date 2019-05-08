from django.db import models

# 用户表，用来记录用户信息
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    nickname = models.CharField(max_length=255)
    avatar_url = models.CharField(max_length=255)
    gender = models.IntegerField()
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    language = models.CharField(max_length=255)

# 活动表，用来记录活动信息
class Activity(models.Model):
    id = models.IntegerField(primary_key=True)
    tag = models.CharField(max_length=255)
    address_final = models.CharField(max_length=255)
    time_on = models.DateTimeField()
    time_up = models.DateTimeField()
    is_finish = models.IntegerField()

# 推荐地点表
class PreferredLocation(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=45)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    score = models.IntegerField()

# 投票信息表
class Voting(models.Model):
    id = models.IntegerField(primary_key=True)
    address_id = models.ForeignKey(PreferredLocation, on_delete=models.CASCADE)
    choose = models.CharField(max_length=3)
    num = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

# 用户活动表，用来记录用户在参与一次活动中的数据
class UserActivity(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
    address_start = models.CharField(max_length=255)
    voting_id = models.ForeignKey(Voting, on_delete=models.CASCADE)
    estimated_time = models.TimeField()
    # uid和aid做联合主键
    class Meta:
        unique_together = ("user_id", "activity_id")

# 常见问题表
class CommonProblem(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

# 广告位表
class Adv(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

# 广告库
class AdvWare(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    adv_id = models.ForeignKey(Adv, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()