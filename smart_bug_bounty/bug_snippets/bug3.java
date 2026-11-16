public class UserAuthenticator {

    public static boolean isAdminUser(String username, String role) {
        // Bug 1: Using `==` instead of `.equals()` for String content comparison
        // Bug 2: Calling `.toLowerCase()` before null check triggers NullPointerException
        String normalizedRole = role.toLowerCase();

        if (username != null && normalizedRole == "admin") {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        String roleFromInput = new String("ADMIN");
        System.out.println(isAdminUser("alice", roleFromInput)); // Expected: true
        System.out.println(isAdminUser("bob", null));            // Expected: false
    }
}
