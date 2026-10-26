package demo;

@RestController
public class UserController {
    @GetMapping("/find")
    public String find(@RequestParam String name) throws Exception {
        String q = "SELECT * FROM users WHERE name = '" + name + "'";
        return jdbc.queryForObject(q, String.class);
    }
    private Cipher cipher() throws Exception {
        return Cipher.getInstance("AES");
    }
}
