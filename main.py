import AI_interface
import config
from UnitTests.BaseUnitTest import runTest
from UnitTests.verifyShopDropRate import verifyShopDropRate 


def main():
    if config.RUN_UNIT_TEST:
        runTest()
        
    if config.RUN_VERIFY_SHOP_DROP_RATE:
       verifyShopDropRate()
       
   # AI_interface.train_model()


if __name__ == "__main__":
    main()
