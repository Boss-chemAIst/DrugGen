def main():
    from models import molecular_VAE, \
                       biological_VAE

    molecular_VAE.main()
    biological_VAE.main()


if __name__ == '_main__':
    main()
