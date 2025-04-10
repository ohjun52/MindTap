import mark_analysis
from login import login

res = login()
if res == 1:
	mark_analysis.get_mark()
elif res == 2:
	mark_analysis.mark_init()