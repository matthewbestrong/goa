# 1. Calculate how many pages a printer will print
def paperwork(n, m):
    return max(n, 0) * max(m, 0)  # თუ რომელიმე რიცხვი უარყოფითია, აბრუნებს 0-ს
