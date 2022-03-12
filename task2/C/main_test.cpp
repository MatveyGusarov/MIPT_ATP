#include "A/index.h"
#include "B/lib.h"
#include "gtest/gtest.h"

TEST(ok,test1) {
    EXPECT_EQ(false, OK(true)); 
}

TEST(less,test1) {
    EXPECT_EQ(false, isOk(true));
}

int main(int argc, char *argv[]) {
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}
