import pandas as pd

def main():
	print("reading/filtering data...")
	# read in constituents data, emails data and subscriptions data
	df_cons=pd.read_csv(r'data/cons.csv', usecols=['cons_id', 'firstname',
                                               'middlename', 'lastname',
                                              'source', 'subsource', 'create_dt', 'modified_dt'])
	emails=pd.read_csv(r'data/cons_email.csv', usecols=['cons_email_id', 'cons_id',
                                                    'cons_email_type_id',
                                                    'is_primary', 'email',])
	subs = pd.read_csv(r'data/cons_email_chapter_subscription.csv')
	# we only care about cons with subscription chapter_id == 1
	subs = subs[subs.chapter_id==1]
	# join subs and email lists on cons_email_id
	subs_emails = subs.join(emails.set_index('cons_email_id'),
                on='cons_email_id',
                how='left',
                lsuffix='_sub_status', rsuffix='_email')
	# join subs,emails with constituents data on cons_id
	alldata = subs_emails.join(df_cons.set_index('cons_id'), on='cons_id',
							  how='left', lsuffix='subsemails',rsuffix='cons')
	# ensure we only have data where chapter_id is 1
	assert (alldata['chapter_id']==1).all()
	# convert 1/0 columns to booleans
	alldata.isunsub = alldata.isunsub.apply(lambda x: x==True)
	
	print("creating people.csv")
	#rename data cols for 'people' report
	# *** Assumption ***
	#	 I'm not sure what "code" is from these datasets but the instructions
	#	 describe it as a "source code", so I'm using "source" from the 
	#	 constituents file as that value
	alldata=alldata.rename(columns={"source": "code", "isunsub": "is_unsub",
                                "create_dt": "created_dt", "modified_dtcons": "updated_dt"})
	alldata.to_csv('people.csv',index=False, columns=['email','code','is_unsub','created_dt','updated_dt'])
	
	# next, create the acquisition_facts CSV to count
	# the number of constituents acquired (created_dt) on each calendard day
	# *** Assumptions ***
	# 	1) we are should still be working with the same
	#	dataset where we "only care about" data where chapter_id is 1
	#	2) we consider a constituent "acquired" when their record was created
	# 	and marked by created_dt
	print("creating acquisition_facts.csv")
	alldata['acquisitions']=1
	alldata['acquisition_date']=pd.to_datetime(alldata.created_dt,
                                                  infer_datetime_format=True)
	alldata['acquisition_date']=alldata['acquisition_date'].apply(lambda x: x.date())
	alldata.groupby('acquisition_date').sum().to_csv('acquisition_facts.csv',
                                                columns=['acquisitions'])

if __name__=='__main__':
	main()