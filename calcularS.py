from Crypto.Hash import SHA256

dec_a = 1437164750761605896701117613557156711703278328311910170042266207183552797139995898043534547594174289402292831101412633084981942889105557808587999290485070339209987904875898562467552403708869055525271608388217500018083529186752709686449691968589037246150975888355122424681103568576623713654541411202331
dec_p = 124325339146889384540494091085456630009856882741872806181731279018491820800119460022367403769795008250021191767583423221479185609066059226301250167164084041279837566626881119772675984258163062926954046545485368458404445166682380071370274810671501916789361956272226105723317679562001235501455748016154805420913

hex_B = "1EE599AE47AD15E4CB59F0A5B6F84108D51584D01A8B58FD302FCC472E8F89DC63833AA2F0409089A740A31A81BB695D03663696E3A6998F8E1BC19E0EB92849C2347602DF2353D79C20B3C374F9AE60E3FEBD4A01326342F882A332287FFD05741F80F338A8C79CBC5F4F3BA9426FAA2EE8CF5325D497E1BDC17AD27F2F73A2"
dec_B = int(hex_B, 16)

dec_V = pow(dec_B, dec_a, dec_p)

S = SHA256.new(str(dec_V).encode('utf-8'))
print(S.hexdigest()[:16])
