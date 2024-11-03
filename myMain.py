#from Peripherals import Peripherals
from myServer import Server
import time

def main():
    # Initialize peripherals and server
    peripherals = Peripherals()
    server = Server(peripherals)
    
    try:
        # keep the server open until a keyboard interrupt is initiated
        while True:
            try:
                print("Starting TCP server...")
                server.start_tcp_server()
            except KeyboardInterrupt:
                print("Shutting down server...")
                break
            except Exception as e:
                print(f"Connection error: {e}")
                print("Attempting to reconnect in 5 seconds...")
                time.sleep(5)  # Wait 5 seconds before attempting to reconnect
            finally:
                server.close()  # Close the server if an error occurs or on shutdown
    except KeyboardInterrupt:
        print("Server stopped manually.")

    # Ensure all resources are cleaned up on exit
    peripherals.cleanup()

if __name__ == "__main__":
    main()
