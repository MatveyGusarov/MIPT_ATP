#include "A/index.h"
#include "B/lib.h"
#include "gtest/gtest.h"

TEST(ok,test1) {
    EXPECT_EQ(false, Invert(true)); 
}

TEST(less,test1) {
    EXPECT_EQ(true, isNormal(true));
}

int main(int argc, char *argv[]) {
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}
