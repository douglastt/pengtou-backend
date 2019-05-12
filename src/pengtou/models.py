from django.db import models

# 用户表，用来记录用户信息
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    nickname = models.CharField(max_length=255, null=True)
    nickname = models.CharField(max_length=255, null=True)
    avatar_url = models.CharField(max_length=255, null=True)
    gender = models.IntegerField(null=True)
    province = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=255, null=True)

# 活动表，用来记录活动信息
class Activity(models.Model):
    id = models.IntegerField(primary_key=True)
    tag = models.CharField(max_length=255, null=True)
    address_final = models.CharField(max_length=255, null=True)
    time_on = models.DateTimeField(null=True)
    time_up = models.DateTimeField(null=True)
    is_finish = models.IntegerField(null=True)

# 推荐地点表
class PreferredLocation(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=45, null=True)
    name = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    score = models.IntegerField(null=True)

# 投票信息表
class Voting(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.ForeignKey(PreferredLocation, on_delete=models.CASCADE)
    choose = models.CharField(max_length=3, null=True)
    num = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

# 用户活动表，用来记录用户在参与一次活动中的数据
class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    address_start = models.CharField(max_length=255, null=True)
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE, null=True)
    estimated_time = models.TimeField(null=True)
    # uid和aid做联合主键
    class Meta:
        unique_together = ("user", "activity")

####################################### 以下模型暂时不用 ############################################
# 常见问题表
class CommonProblem(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.TextField(null=True)
    answer = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

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
    adv = models.ForeignKey(Adv, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()