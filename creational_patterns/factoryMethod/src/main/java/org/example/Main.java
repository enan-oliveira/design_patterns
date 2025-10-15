package org.example;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    static void main() {

        NotificationFactory factory;

        String tipo = "push";

        switch (tipo.toLowerCase()) {
            case "email":
                factory = new EmailFactory();
                break;
            case "sms":
                factory = new SMSFactory();
                break;
            case "push":
                factory = new PushFactory();
                break;
            default:
                throw new IllegalArgumentException("Tipo de notificação inválido");
        }

        factory.sendNotification();
    }
}
