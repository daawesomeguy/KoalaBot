package KoalaBot.KoalaBot.commands;

import com.jagrosh.jdautilities.command.Command;
import com.jagrosh.jdautilities.command.CommandEvent;

public class Ping extends Command{
	public Ping() {
		this.name = "ping";
		this.help = "pong";
				
	}
	@Override
	protected void execute(CommandEvent e) {
		e.reply("pong");
		
	}

}
