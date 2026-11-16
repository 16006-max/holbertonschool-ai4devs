public class UserAuthenticator {

    public static boolean isAdminUser(String username, String role) {
        // Fixed: Check for null values before calling String methods
        if (username == null || username.trim().isEmpty() || role == null) {
            return false;
        }

        // Fixed: Use `.equalsIgnoreCase()` for content comparison instead of `==`
        return "admin".equalsIgnoreCase(role.trim());
    }

    public static void main(String[] args) {
        String roleFromInput = new String("ADMIN");
        assert isAdminUser("alice", roleFromInput) : "Test 1 failed";
        assert !isAdminUser("bob", null) : "Test 2 failed";
        assert !isAdminUser(null, "admin") : "Test 3 failed";
        assert !isAdminUser("charlie", "user") : "Test 4 failed";
        System.out.println("All bug3_fixed.java test cases passed!");
    }
}
