from django.db import models


MONTHS = {	1: 'January',
			2: 'February',
			3: 'March',
			4: 'April',
			5: 'May',
			6: 'June',
			7: 'July',
			8: 'August',
			9: 'September',
			10: 'October',
			11: 'November',
			12: 'December'}

# Create your models here.
class Month(models.Model):
	"""
	We might want to use this to determine what to work on
	EG wanna see all jobs for March without searching each possible task
	(planting, harvest etc) individually

	If we do, let's use the ID as the month number - so January = 1, December = 12
	We can make sure that happens using fixtures :)

	For now on the Plant I'll just use an Integer field rather than FK to a month
	"""
	@property
	def name(self):
		return MONTHS[self.id]

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['id']

# for m in range(1,len(MONTHS)+1):
#     Month.objects.create(name=MONTHS[m-1],id=m)