package KoalaBot.KoalaBot;

import javax.security.auth.login.LoginException;

import com.jagrosh.jdautilities.command.CommandClient;
import com.jagrosh.jdautilities.command.CommandClientBuilder;
import com.jagrosh.jdautilities.commons.waiter.EventWaiter;

import KoalaBot.KoalaBot.commands.Bestflip;
import KoalaBot.KoalaBot.commands.Petflip;
import KoalaBot.KoalaBot.commands.Ping;
import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.OnlineStatus;

public class Koala {
	public static final String prefix = "-";
	public static void main(String[] args) throws LoginException {
		JDA jda = JDABuilder.createDefault("NzYwNDc5MjQ3NTc5NDgwMDg2.X3MpfQ.Gnm_q982rxCqDM1w-nN2VxlzY2o").build();
		
		EventWaiter waiter = new EventWaiter();
		
		CommandClientBuilder builder = new CommandClientBuilder();
		
		builder.setOwnerId("760479247579480086");
		builder.setPrefix("-");
		builder.setHelpWord("help");
		builder.setStatus(OnlineStatus.ONLINE);
		
		builder.addCommand(new Ping());
		builder.addCommand(new Petflip());
		builder.addCommand(new Bestflip());
		
		CommandClient client = builder.build();
		
		jda.addEventListener(client);
		jda.addEventListener(waiter);
	}
}
