"""Alert handlers"""
import aiohttp
from typing import Optional

class TelegramAlerts:
    def __init__(self, config: dict):
        self.bot_token = config.get('bot_token')
        self.chat_ids = config.get('alert_chat_ids', [])
        
    async def send(self, message: str):
        """Send to all configured chats"""
        if not self.bot_token:
            return
            
        for chat_id in self.chat_ids:
            async with aiohttp.ClientSession() as sess:
                await sess.post(
                    f"https://api.telegram.org/bot{self.bot_token}/sendMessage",
                    json={
                        'chat_id': chat_id,
                        'text': message,
                        'parse_mode': 'HTML'
                    }
                )
                
    async def whale_alert(self, activity):
        """Whale activity alert"""
        msg = f"""🐋 WHALE ALERT
━━━━━━━━━━━━━━━━━━
{activity.chain.upper()}
{activity.token}
Amount: {activity.amount:,.0f}
${activity.usd_value:,.0f}
Type: {activity.activity_type}
{activity.tx_hash}
━━━━━━━━━━━━━━━━━━"""
        await self.send(msg)
        
    async def new_pool_alert(self, pool):
        """New pool detected"""
        msg = f"""🎯 NEW POOL
━━━━━━━━━━━━━━━━━━
{pool.base_token}/{pool.quote_token}
Liquidity: ${pool.liquidity_usd:,.0f}
MC: ${pool.mc_fdv:,.0f}
Pool: {pool.pair_address}
━━━━━━━━━━━━━━━━━━"""
        await self.send(msg)