#include <test.h>

#include <scope.h>
#include <eval_context.h>
#include <rlist.h>

static void test_name_join(void)
{
    {
        char buf[CF_MAXVARSIZE] = { 0 };
        JoinScopeName(NULL, "sys", buf);
        assert_string_equal("sys", buf);
    }

    {
        char buf[CF_MAXVARSIZE] = { 0 };
        JoinScopeName("ns", "b", buf);
        assert_string_equal("ns:b", buf);
    }
}

int main()
{
    const UnitTest tests[] =
{
        unit_test(test_name_join),
    };

    PRINT_TEST_BANNER();
    return run_tests(tests);
}
