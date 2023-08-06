import tkinter as tk
import tkinter.filedialog
from tkinter import Label, Menu, Toplevel, ttk
import csv
import requests
from bs4 import BeautifulSoup
import time

# Create the main window
root = tk.Tk()
root.iconbitmap("icon/icon.ico")
root.title("Web Scraper")
root.geometry("800x600")
# root.configure(bg='#D3D3D3')
bgimg = tk.PhotoImage(file="icon.png")
limg = Label(root, i=bgimg)
limg.pack(side=tk.TOP)

# Creating a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Adding a file menu
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)


# Adding a help menu
help_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Guide",
                      command=lambda: display_help_window(root))

# Read the contents of the file
with open("help.txt", "r") as file:
    content = file.read()


def display_help_window(root):
    help_window = Toplevel(root)
    help_window.title("Help Topics")
    help_window.geometry("400x400")
    help_label = Label(help_window, text=f"{content}")

    help_label.pack()


# Adding Contact Us Menu
contact_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Contact us", menu=contact_menu)
contact_menu.add_command(label="Contact us",
                         command=lambda: display_contact_window(root))


def display_contact_window(root):
    contact_window = Toplevel(root)
    contact_window.title("Help Topics")
    contact_window.geometry("400x400")
    help_label = Label(
        contact_window, text="Contact us in : Ayoubleepro@gmail.com")

    help_label.pack()


website_var = tk.StringVar(value="ebay")
website_options = ['ebay', 'amazon', 'jumia']

# Scrape Data

def scrape():
    global products
    products = []
    website = website_var.get()
    keyword = entry.get()
    if website == "ebay":
        url = f"https://www.ebay.com/sch/i.html?_nkw={keyword}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        items = soup.find_all('div', class_="s-item__info clearfix")
        textbox.delete(1.0, tk.END)
        for item in items:
            price = item.find(class_='s-item__price')
            if price:
                price = price.text
            else:
                price = "Not available"
            description = item.find('div', class_="s-item__title")
            if description:
                description = description.text
            else:
                description = "Not available"
            link = item.find('a')
            if link:
                link = link['href']
            else:
                link = "Not available"
            products.append({"description": description,
                            "price": price, "link": link})
            textbox.insert(
                tk.INSERT, f"Price: {price}\nDescription: {description}\nLink: {link}\n\n")
    elif website == "amazon":
        url = f"https://www.amazon.com/s?field-keywords={keyword}"

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding": "gzip, deflate",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        items = soup.find_all(
            'div', class_='a-section a-spacing-small a-spacing-top-small')
        textbox.delete(1.0, tk.END)
        for item in items:

            price = item.find('span', class_='a-offscreen')
            if price:
                price = price.text
            else:
                price = "Not available"
            description = item.find(
                class_='a-size-base-plus a-color-base a-text-normal')
            if description:
                description = description.text
            else:
                description = "Not available"
            link = item.find('a')
            if link:
                link = link['href']
            else:
                link = "Not available"
            textbox.insert(
                tk.INSERT, f"Price: {price}\nDescription: {description}\nLink: {link}\n\n")
    elif website == "jumia":
        url = f"https://www.jumia.ma/catalog/?q={keyword}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        items = soup.find_all('div', class_="info")
        textbox.delete(1.0, tk.END)
        for item in items:
            title = item.find('h3', class_='name')
            price = item.find('div', class_='prc')
            stars = item.find('div', class_='stars _s')
            if title is not None:
                title = title.text
            else:
                title = "Title not found"
            if price is not None:
                price = price.text
            else:
                price = "Price not found"
            if stars is not None:
                stars = stars.text
            else:
                stars = "Stars not found"
            textbox.insert(
                tk.INSERT, f"Price: {price}\nTitle: {title}\nStars: {stars}\n\n")


# Save results to CSV:

def save_to_csv():
    filename = tkinter.filedialog.asksaveasfilename(
        defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        website = website_var.get()
        website == "ebay" or "amazon"
        writer.writerow(["Product", "Price", "Link"])
        for product in products:
            writer.writerow(
                [product["description"], product["price"], product["link"]])


file_menu.add_command(label="Export to CSV file", command=save_to_csv)

# Adding an exit menu
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create a frame for the keyword input and the scrape button
input_frame = tk.Frame(root, bg='#D3D3D3')
input_frame.pack(pady=20)


label = tk.Label(input_frame, text="Enter keyword:",
                 bg='grey', fg='black')
label.pack(side=tk.LEFT, padx=10)

entry = tk.Entry(input_frame, width=50)
entry.pack(side=tk.LEFT, padx=10)

website_dropdown = tk.OptionMenu(
    root, website_var, *website_options)  # .place(x=380, y=45)
website_dropdown.config(bg='grey', fg='#FFFFFF')
website_dropdown.pack(side=tk.TOP, padx=200)

scrape_button = tk.Button(text="Scrape", command=lambda: [
                          scrape(), start_progress()], bg='black', fg='#FFFFFF', relief=tk.RAISED)  # .place(x=610, y=18)
scrape_button.pack(side=tk.TOP, padx=1,)

# Create a frame for the scraped data
data_frame = tk.Frame(root, bg='#D3D3D3')
data_frame.pack(pady=20)

# Create a scrollbar for the text box
scrollbar = tk.Scrollbar(data_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a text box to display the scraped data
textbox = tk.Text(data_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, font=(
    "Helvetica", 12), width=50, height=20, bg='#FFFFFF')
scrollbar.config(command=textbox.yview)
textbox.pack()

# Create progress bar

progress = tk.ttk.Progressbar(
    root, orient='horizontal', length=400, mode='determinate')
progress.pack()


def start_progress():
    progress['value'] = 0
    progress['maximum'] = 100
    progress_var = tk.StringVar(value="Scraping....")
    progress_label = tk.Label(
        root, textvariable=progress_var, bg='#57DCBE', fg='blue')
    progress_label.pack()

    for i in range(101):
        progress_var.set("Scraping... %d%%" % i)
        progress['value'] = i
        root.update_idletasks()
        time.sleep(0.01)
    progress.pack_forget()
    progress_label.pack_forget()


root.mainloop()