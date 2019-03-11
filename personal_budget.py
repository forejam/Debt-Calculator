#---------------------------|
# a personal debt calculator 
# jamie fore
#---------------------------|

import ui
# from console import hud_alert

# i/o
history = open('history.txt', 'r+')
rec = history.readline()
fields = rec.split(',')
		
# pay or purchase
def button_pushed(sender):
	'@type sender: ui.Button'
	t = sender.title
	
	if t == 'Pay':
		# dollar amount typed
		txt_amt = v['text_amount']
		inpt = txt_amt.text
		if inpt.strip() != '':
			# debit or credit
			deb_or_cred = v['pmt_type']
			pos = deb_or_cred.selected_index
			# determines record to update
			if pos == 0:
				curr = fields[0]
			elif pos == 1:
				curr = fields[1]
			new_amt = calculate(t,curr,inpt)
			fupdate(inpt, new_amt)		
	elif t == 'Purchase':
		# dollar amount typed
		txt_amt = v['text_amount']
		inpt = txt_amt.text
		if inpt.strip() != '':
			# debit or credit
			deb_or_cred = v['pmt_type']
			pos = deb_or_cred.selected_index
			# determines record to update
			if pos == 0:
				curr = fields[0]
			elif pos == 1:
				curr = fields[1]
			new_amt = calculate(t,curr,inpt)
			fupdate(inpt, new_amt)

# calculates the difference or sum
def calculate(type, current, new):
	# pay or purchase
	if type == 'Pay':
		return float(current) + float(new)
	elif type == 'Purchase':
		return float(current) - float(new)
		
# updates fields and files
def fupdate(amt, tot):
	# debit or credit
	deb_or_cred = v['pmt_type']
	pos = deb_or_cred.selected_index
	
	# updates the fields
	fields[pos] = str('{0:.2f}'.format(tot))
	if pos == 0:
		txt_bnk.text =  '$' + fields[0]
	elif pos == 1:
		txt_crd.text =  '$' + fields[1]
		
	# updates the total
	txt_tot = v['text_total']
	new_tot = float(fields[0]) + float(fields[1])
	fields[2] = str('{0:.2f}'.format(new_tot))
	txt_tot.text =  '$' + fields[2]
	
	# updates the file
	new_rec = fields[0] + ',' + fields[1] + ',' + fields[2]
	history.seek(0,0)
	history.write(new_rec)
	
v = ui.load_view()

# text field initializations
txt_bnk = v['text_bank']
txt_bnk.text =  '$' + fields[0]

txt_crd = v['text_credit']
txt_crd.text =  '$' + fields[1]

txt_tot = v['text_total']
txt_tot.text =  '$' + fields[2]

# determines screen resolution
if min(ui.get_screen_size()) >= 768:
	# iPad
	v.frame = (0, 0, 360, 400)
	v.present('sheet')
else:
	# iPhone
	v.present(orientations=['portrait'])
