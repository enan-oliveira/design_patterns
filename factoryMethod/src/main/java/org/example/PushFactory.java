package org.example;

class PushFactory extends NotificationFactory {
    public Notification createNotification() {
        return new PushNotification();
    }
}
