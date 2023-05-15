import discord


def send_message(name_1):
    name = 'member'

    if name == 'member':
        TOKEN = "MTA3ODczMDEyODk1NzM3ODY0Mg.GR2mdo.7npwXg8bvDRq3zDTfn6rvh_6RJv3J1rj14MDZM"
        status = 'member'
        intents = discord.Intents.default()
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            channel = client.get_channel(1078722332446707762)
            await channel.send(f"{name_1} has entered the lab")

        client.run(TOKEN)