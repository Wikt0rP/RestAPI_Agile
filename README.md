# RestAPI_CashFlow
Requests:

//

//

SAVINGS
 
//


savings/                                                          ____________ all savings

savings/id=<int:pk>/                                              ____________ savings by savingID

savings/walletID=<int:walletID>/                                  ____________ saving by walletID

savings/update/id=<int:pk>/add=<int:value>/                       ____________ add cash to savings

savings/update/id=<int:pk>/remove=<int:value>/                    ____________ remove cash from savings

//

//

GROUPS

//

group/create/ _________ create group headers: auth & name

group/																														____________ all groups

group/user=<int:pk>/																							____________ user's groups

group=<id_grupy>/adduser=<id_uzytkownika>													____________ add user to group

group=<id_grupy>/deleteuser=<id_uzytkownika>											____________ remove user from group

//

//

HISTORY

//

history/																													____________ transactions history

history/transactionID=<int:pk>																		____________ get transaction by id

history/walletID=<int:pk>																					____________ get all wallet's transactions

//

//

MAILS

//

mail/																													____________ get all mails

mail/userid=<odbiorcaID>																			____________ get mails by userID

mail/read/<pk>																								____________ mark mail as read

//

//

WALLET

//

wallet/create/   ____________ create wallet for userID

wallets/ ____________ list all wallets

sendtransfer/  ____________ send transfer  headers: "Authorization", "TargetWallet", "Money"

//


//

USER AND AUTHENTICATION

//

getuser/																													____________ get info about user by jwt token

jwt/create																												____________ create JWT Token

jwt/verify																												____________ verify token

users/																													____________ create user
/users/

//

STANDING ORDERS

//
standingOrder/create ____________ Create standing order ______ headers: "Authorization", "money", "title", "day"  (day of the transfer execution), "TargetWalletID"

standingOrder/user ____________ Get user's standing orders ______ headers: "Authorization"

standingOrder/internal ____________ Create standing order for your own wallet -  that's income headers: "Authorization", "money", "title", "day" (day of the transfer execution)

standingOrder/update ____________ Update standing order data  FOR PATCH: headers (* - obligatory ): "Authorization"*, "orderID"*, "money", "title", "day" FOR DELETE: "Authorization"*, "orderID"*

//
//

//

//

//

//

FROM https://djoser.readthedocs.io/en/latest/getting_started.html#available-endpoints:

//

/users/me/

/users/confirm/

/users/resend_activation/

/users/set_password/

/users/reset_password/

/users/reset_password_confirm/

/users/set_username/

/users/reset_username/

/users/reset_username_confirm/

/token/login/ (Token Based Authentication)

/token/logout/ (Token Based Authentication)

/jwt/create/ (JSON Web Token Authentication)

/jwt/refresh/ (JSON Web Token Authentication)

/jwt/verify/ (JSON Web Token Authentication)

