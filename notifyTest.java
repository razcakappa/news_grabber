import org.gnome.gtk.Gtk;
import org.gnome.notify.Notification;
import org.gnome.notify.Notify;

public class notifyTest {
    public static void main(String[] args) {  

        Gtk.init(args); // initialize Gtk
        Notify.init("Program Name"); // initalize the notification system  

        Notification myNotification = new Notification("Hello world!", "This is an example notification.", "dialog-information"); // create the notification object
        myNotification.show(); // show the notification  

    }


}
