customers = {}
balances = {}

def validate_account_number(account_number):
    return (len(account_number)==5 and account_number.startswith('TB') and account_number[2:].isdigit())

# შევქმენი სხვადასხვა მოდულები სხვადასსხვა ოპერაციების შესასრულებლად
# ერთი არეგისტრირებს მომხმარებელს და ერთი ბალანსს ავსებინებს და ასევე ტრანზაქციებს ასრულებინებს მომხმარებელს
# უბრალოდ ვფიქრობ, რომ სამივე კოდი ერთმანეთთან ისე ვერ დავაკავშირე როგორც საჭიროა 
# ამ პრობლემის მოგვარების გზას feedback-ში დიდი სიამოვნებით ვიხილავდი 