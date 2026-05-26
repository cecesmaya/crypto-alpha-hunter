"""
🦁 Crypto Alpha Hunter - Main Scanner
Real-time whale tracking and alpha detection
"""
import asyncio
import logging
import yaml
from pathlib import Path

from src.whale_tracker import WhaleTracker
from src.snipe_detector import SnipeDetector
from src.rug_checker import RugChecker
from alerts import TelegramAlerts

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s 🦁 %(message)s'
)
log = logging.getLogger(__name__)

class AlphaHunter:
    def __init__(self, config_path: str = "config.yaml"):
        with open(config_path) as f:
            self.config = yaml.safe_load(f)
            
        self.whale_tracker = WhaleTracker(self.config)
        self.snipe_detector = SnipeDetector(self.config)
        self.rug_checker = RugChecker(self.config)
        self.alerts = TelegramAlerts(self.config.get('telegram', {}))
        
    async def start(self):
        """Start the alpha hunter"""
        log.info("🦁 Starting Crypto Alpha Hunter...")
        log.info("📡 Monitoring %d chains", len(self.config.get('chains', {})))
        
        while True:
            try:
                # Track whale movements
                activities = await self.whale_tracker.monitor_all()
                for activity in activities:
                    if activity.usd_value >= self.config.get('alerts', {}).get('min_volume_usd', 10000):
                        await self.alerts.whale_alert(activity)
                        
                # Check for new pools
                new_pools = await self.snipe_detector.check_pair_created("solana")
                for pool in new_pools:
                    if self.snipe_detector.should_snip(pool):
                        await self.alerts.new_pool_alert(pool)
                        
                await asyncio.sleep(self.config.get('scanner', {}).get('poll_interval', 5))
                
            except Exception as e:
                log.error("Error: %s", e)
                await asyncio.sleep(5)

def main():
    import sys
    config_path = sys.argv[1] if len(sys.argv) > 1 else "config.yaml"
    
    hunter = AlphaHunter(config_path)
    asyncio.run(hunter.start())

if __name__ == "__main__":
    main()

# Commands:
# /start      - Initialize
# /track     - Add wallet  
# /alert     - Configure alerts
# /status    - System status